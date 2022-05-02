/**
 * Script     : Bring Back Those Dead Soldiers
 * Author     : obez
 * Description: Brings back the dead bodies of survivors
 * Thanks to  : 
 *   Leeland (http://www.leeland.net/l4d2-scripting.html)
 *   HelmsDeepReborn Script for the "survivor_death_model" class.
 *
 * Used in the Survival map
 */
tpPosIt <- 1;
deadSurvivor <- Entities.FindByClassname(null, "survivor_death_model");

while (deadSurvivor != null) {
  survRescueName <- "survivor_rescue_"+tpPosIt++;
  tpDestOrigin <- Entities.FindByName(null, survRescueName).GetOrigin();
  deadSurvOrigin <- deadSurvivor.GetOrigin();
  deadSurvivor.SetOrigin(tpDestOrigin);
  deadSurvivor <- Entities.FindByClassname(deadSurvivor, "survivor_death_model");
}
