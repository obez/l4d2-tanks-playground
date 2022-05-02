/**
 * Script     : Bring Back Those Dead Soldiers
 * Author     : obez
 * Description: Brings back the dead bodies of survivors who have drowned
 * Thanks to  : 
 *   Leeland (http://www.leeland.net/l4d2-scripting.html)
 *   HelmsDeepReborn Script for the "survivor_death_model" class.
 *
 * Used in the Campaign map
 */
DROWNED_SURV_MAX_Z <- -360;

tpPosIt <- 1;
deadSurvivor <- Entities.FindByClassname(null, "survivor_death_model");

while (deadSurvivor != null) {
  tpDestOrigin <- Entities.FindByName(null, "survivor_rescue_"+tpPosIt++).GetOrigin();
  deadSurvOrigin <- deadSurvivor.GetOrigin();
  
  // Only move drowned survivors
  if( deadSurvOrigin.z < DROWNED_SURV_MAX_Z ) {
    deadSurvivor.SetOrigin(tpDestOrigin);
    EntFire("relay_dead_player_teleported", "Trigger", 0);
  }

  deadSurvivor <- Entities.FindByClassname(deadSurvivor, "survivor_death_model");
}
