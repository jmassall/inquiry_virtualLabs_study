#Checking  implementation of python cronbach alpha
setwd("C:/Users/Sarah/git/inquiry_virtualLabs_study/")
d <- read.table("parsing_survey/quant_posts_scores_floored.txt", header = TRUE, sep="\t")
#d <- read.table("parsing_survey/qual_posts_scores.txt", header = TRUE, sep="\t")
d$sid = NULL
d$sid.1 = NULL
d$activity.order = NULL
str(d)
psych::alpha(d)
psych::alpha(d)$total$std.alpha

library("sjPlot")
sjt.itemanalysis(d)



d <- read.csv("analysis/dataframe_all_incoming_factors_by_student.csv", header = TRUE, sep=",")
str(d)
sjt.itemanalysis(d[,c("pocc.0.learning.the.basic.concepts","pocc.1.testing.my.ideas.and.theories","pocc.2.answering.given.questions","pocc.3.memorizing.key.information","pocc.4.exploring.the.topic")])
sjt.pca(d[,c("perceivedvalue.0.boring.reversed","perceivedvalue.1.productive","perceivedvalue.2.useless.reversed","perceivedvalue.3.engaging","taskinterpretation.0.investigate.the.basic.mechanics.of.the.topic.at.hand","taskinterpretation.1.design.my.own.experiments.that.can.help.me.understand.the.topic.at.hand","taskinterpretation.2.memorize.information.about.the.topic.at.hand","taskinterpretation.3.complete.a.certain.number.of..questions","taskinterpretation.4.develop.scientific.reasoning.skills")])
d
