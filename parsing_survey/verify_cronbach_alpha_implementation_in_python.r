#Checking  implementation of python cronbach alpha

d <- read.table("C:/Users/Sarah/git/inquiry_virtualLabs_study/parsing_survey/quant_posts_scores_floored.txt", header = TRUE, sep="\t")
#d <- read.table("C:/Users/Sarah/git/inquiry_virtualLabs_study/parsing_survey/qual_posts_scores.txt", header = TRUE, sep="\t")
d$sid = NULL
d$sid.1 = NULL
d$activity.order = NULL
str(d)

psych::alpha(d)
psych::alpha(d)$total$std.alpha

library("sjPlot")
sjt.itemanalysis(d)
