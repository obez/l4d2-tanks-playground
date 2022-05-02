//-----------------------------------------------------------------------------
// Enumerations of stage types
TANK <- 1
 
//-----------------------------------------------------------------------------
// Initialization of tables that will be fed to DirectorOptions
 
DirectorOptions <-
{
  // Additional Director options
  ShouldConstrainLargeVolumeSpawn = false
 
  ZombieSpawnRange = 100
 
  SpecialRespawnInterval = 6000
  
  TankLimit = 30
  WitchLimit = 0
  CommonLimit = 0
  SmokerLimit = 0
  SpitterLimit = 0
  HunterLimit = 0
  JockeyLimit = 0
  BoomerLimit = 0
  ChargerLimit = 0
  ShouldAllowSpecialsWithTank = false
  PreferredMobDirection = SPAWN_ANYWHERE
  PreferredSpecialDirection = SPAWN_SPECIALS_ANYWHERE
  BehindSurvivorsSpawnDistance = 2000

  A_CustomFinale_StageCount = 10

  A_CustomFinale1 = TANK
  A_CustomFinaleValue1 = 20
  A_CustomFinale2 = TANK
  A_CustomFinaleValue2 = 20
  A_CustomFinale3 = TANK
  A_CustomFinaleValue3 = 20
  A_CustomFinale4 = TANK
  A_CustomFinaleValue4 = 20
  A_CustomFinale5 = TANK
  A_CustomFinaleValue5 = 20
  A_CustomFinale6 = TANK
  A_CustomFinaleValue6 = 20
  A_CustomFinale7 = TANK
  A_CustomFinaleValue7 = 20
  A_CustomFinale8 = TANK
  A_CustomFinaleValue8 = 20
  A_CustomFinale9 = TANK
  A_CustomFinaleValue9 = 20
  A_CustomFinale10 = TANK
  A_CustomFinaleValue10 = 20
}