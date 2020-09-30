#include "./immune_submodels.h" 
using namespace PhysiCell; 
std::string immune_submodels_version = "0.0.1"; 
Submodel_Information CD8_submodel_info; 
Submodel_Information Macrophage_submodel_info; 
Submodel_Information Neutrophil_submodel_info; 

std::vector<int> vascularized_voxel_indices;

void macrophage_phenotype( Cell* pCell, Phenotype& phenotype, double dt )
{
	static int apoptosis_index = phenotype.death.find_death_model_index( "Apoptosis" ); 
	static Cell_Definition* pCD = find_cell_definition( "macrophage" ); 
	static int proinflammatory_cytokine_index = microenvironment.find_density_index( "pro-inflammatory cytokine");
	static int chemokine_index = microenvironment.find_density_index( "chemokine");
	static int debris_index = microenvironment.find_density_index( "debris");
			
	// determine bias_direction for macrophage based on "eat me" signals and chemokine
	double sensitivity_chemokine = pCell->custom_data["sensitivity_to_chemokine_chemotaxis"];
	double sensitivity_eat_me = pCell->custom_data["sensitivity_to_eat_me_chemotaxis"];

	pCell->phenotype.motility.migration_bias_direction = sensitivity_chemokine*pCell->nearest_gradient(chemokine_index)+sensitivity_eat_me*pCell->nearest_gradient(debris_index);
	normalize( &( phenotype.motility.migration_bias_direction) );

	// make changes to volume change rate??
	// if too much debris, comit to apoptosis 	
	double relative_volume = ( phenotype.volume.total/pCD->phenotype.volume.total ); 
	if( relative_volume > pCell->custom_data[ "relative_maximum_volume" ] )
	{
		pCell->start_death( apoptosis_index ); 
		pCell->phenotype.secretion.secretion_rates[proinflammatory_cytokine_index] = 0; 
		pCell->phenotype.secretion.secretion_rates[debris_index] = pCell->custom_data["debris_secretion_rate"]; 

//		std::cout << " I ate to much and must therefore die " << std::endl; 
//		system("pause"); 
		// Paul on June 5, 2020: do you want a "return" here? 
		return;
	}
	// check for cells to eat 
	std::vector<Cell*> neighbors = pCell->cells_in_my_container();  // rwh_nbrs

	// at least one of the cells is pCell 
	if( neighbors.size() < 2 )
	{ return; } 
	
	double macrophage_probability_of_phagocytosis = pCell->custom_data["macrophage_probability_of_phagocytosis"];
	// Note from Paul on June 5, 2020: this probability depends on dt. 
	// You shoudl chnage it to a rate, so probability = rate * dt 
 
	int n = 0; 
	Cell* pTestCell = neighbors[n]; 
	while( n < neighbors.size() )
	{
		pTestCell = neighbors[n]; 
		// if it is not me and not a macrophage 
		if( pTestCell != pCell && pTestCell->phenotype.death.dead == true && 
			UniformRandom()<macrophage_probability_of_phagocytosis )
		{
//			std::cout << "\t\tnom nom nom" << std::endl; 
//			std::cout << "\t\t\t" << pCell  << " eats " << pTestCell << std::endl; 
			#pragma omp critical(macrophage_eat)
			{
//				std::cout << "\t\t\t" << pCell->type_name << " " << pCell << " eats " 
//				<< pTestCell->type_name << " " << pTestCell << " " << pTestCell->phenotype.volume.total << std::endl; 
				remove_all_adhesions( pTestCell ); // debug 
				pCell->ingest_cell( pTestCell ); 
			}	
				pCell->phenotype.secretion.secretion_rates[proinflammatory_cytokine_index] = 
					pCell->custom_data["activated_macrophage_secretion_rate"]; // 10;
				pCell->phenotype.secretion.uptake_rates[chemokine_index] = 
					pCell->custom_data["activated_cell_chemokine_uptake_rate"]; // 10;
				pCell->phenotype.secretion.uptake_rates[proinflammatory_cytokine_index] = 
					pCell->custom_data["activated_cell_cytokine_uptake_rate"]; // 10;
				pCell->phenotype.secretion.uptake_rates[debris_index] = 
					pCell->custom_data["activated_cell_chemokine_uptake_rate"]; // 10;
      
			pCell->phenotype.motility.migration_speed = 
				pCell->custom_data["activated_macrophage_speed"]; 
			pCell->custom_data["activated_macrophage"] = 1.0; 
//			system("pause");
			return; 
		}
//		else
//		{
//			std::cout << " (" << (int) pTestCell->phenotype.death.dead << " " << 
//			(int) pTestCell->phenotype.flagged_for_removal << ") " ; 
//		}
		n++; 
	}
	return; 
}
void macrophage_mechanics( Cell* pCell, Phenotype& phenotype, double dt )
{
	// bounds check 
	if( check_for_out_of_bounds( pCell , 10.0 ) )
	{ 
		replace_out_of_bounds_cell( pCell, 10.0 );
		return; 
	}	

	return; 
}