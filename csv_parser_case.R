matrixSummarizer <- function(matrixfile,matching_patterns,normalizing_variable,refsample_pattern){
  data_matrix  <- read.table(matrixfile,header=T,sep=',',check.names = F)
  relevant_columns <- vector()
  for(i in 1:length(matching_patterns)){
    relevant_columns <- c(relevant_columns, grep(matching_patterns[i],colnames(data_matrix)))
  }
  rel_matrix <- data_matrix[,unique(relevant_columns)]
  rownames(rel_matrix) <- data_matrix$Sample
  norm_column <- which(colnames(rel_matrix)==normalizing_variable)
  norm_mat <- rel_matrix/rel_matrix[,norm_column]
  relevant_rows <- grep(refsample_pattern,rownames(norm_mat))
  ref_medians <- apply(norm_mat[relevant_rows,],2,median)
  nonref_matrix <- norm_mat[-relevant_rows,]
  for(i in 1:ncol(nonref_matrix)){
    nonref_matrix[,i] <- nonref_matrix[,i]/ref_medians[i]
  }
  return(nonref_matrix)
  }

scaled_matrix <- matrixSummarizer("data_matrix.csv",matching_patterns = c("AG*","IG*","HYC*","UNI*"),normalizing_variable = "HYC01",refsample_pattern = "QCC30_*")
