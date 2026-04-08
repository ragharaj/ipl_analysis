from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType, DoubleType


match_metadata_schema = StructType([
    StructField("id", StringType(), True),
    StructField("season", IntegerType(), True),
    StructField("city", StringType(), True),
    StructField("date", StringType(), True),
    StructField("team1", StringType(), True),
    StructField("team2", StringType(), True),
    StructField("toss_winner", StringType(), True),
    StructField("toss_decision", StringType(), True),
    StructField("result", StringType(), True),
    StructField("dl_applied", IntegerType(), True),
    StructField("winner", StringType(), True),
    StructField("win_by_runs", IntegerType(), True),
    StructField("win_by_wickets", IntegerType(), True),
    StructField("player_of_match", StringType(), True),
    StructField("venue", StringType(), True),
    StructField("umpire1", StringType(), True),
    StructField("umpire2", StringType(), True),
    StructField("umpire3", StringType(), True)
])

people_schema = StructType([
    StructField("player_id", StringType(), False),
    StructField("playner_name", StringType(), True),
    StructField("unique_name", StringType(), True),
    StructField("key_cricinfo", StringType(), True),
])