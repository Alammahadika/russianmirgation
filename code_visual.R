library(ggplot2)
library(ggrepel)

# Create visually enhanced scatter plot of keyword frequencies
ggplot(keywordsmigrationpolicy, aes(x = Selected, y = Occurences)) +
  geom_point(aes(color = ifelse(Keyword %in% c("Media Discourse", "Mass Media"), "red", "black")),
             size = 0, alpha = 0.7) +
  
  # Smart labeling to avoid overlap
  geom_text_repel(aes(label = Keyword, 
                      color = ifelse(Keyword %in% c("Media Discourse", "Mass Media"), 
                                     "red", "black")),
                  size = 3.5,
                  max.overlaps = 30,
                  box.padding = 0.5,
                  segment.color = 'grey50') +
  
  # Trend line
  geom_smooth(method = "loess", se = FALSE, color = "blue", linetype = "dashed") +
  
  # Labels and titles
  labs(title = "Keyword Frequency in Migration Policy Research",
       subtitle = "Analysis of Academic Literature (n = 1,500+ articles)",
       x = "Keyword Categories",
       y = "Frequency Count",
       caption = "Note: Media-related keywords highlighted in red") +
  
  # Visual enhancements
  ylim(min(keywordsmigrationpolicy$Occurences) - 10,
       max(keywordsmigrationpolicy$Occurences) + 10) +
  scale_color_identity() +
  theme_minimal() +
  theme(
    plot.title = element_text(face = "bold", size = 14, hjust = 0.5),
    plot.subtitle = element_text(hjust = 0.5, color = "gray40"),
    panel.grid.major = element_line(color = "gray90"),
    axis.title = element_text(face = "bold")
  )



                        #============#



library(ggplot2)
library(dplyr)

# Data Frame

data <- data.frame(
  individual = c("Political Implication", "External Regulator", "Crime and Punishment", 
                 "Public Sentiment", "Economy", "Justice and Equality", "Safety", 
                 "Quality Life", "Capacity and Resources", "Culture Identity",
                 "Political Implication", "Crime and Punishment", "Safety", 
                 "Capacity and Resources", "Justice and Equality", "External Regulator",
                 "Public Sentiment", "Culture Identity", "Economy", "Quality Life",
                 "Safety", "Political Implication", "Crime and Punishment", 
                 "Public Sentiment", "Capacity and Resources", "Justice and Equality", 
                 "External Regulator", "Economy", "Quality Life", "Culture Identity",
                 "Morality and Ethic", "External Regulator", "Justice and Equality", 
                 "Political Implication", "Economy", "Safety", "Quality Life", 
                 "Capacity and Resources", "Morality and Ethic", "Culture Identity", 
                 "Crime and Punishment", "Public Sentiment", "External Regulator", 
                 "Economy", "Justice and Equality", "Safety", "Capacity and Resources", 
                 "Crime and Punishment", "Quality Life", "Morality and Ethic", 
                 "Public Sentiment", "Culture Identity"),
  value = c(22, 14, 10, 9, 8, 4, 4, 4, 3, 3, 
            15, 15, 15, 15, 11, 8, 7, 6, 5, 4, 
            17, 15, 13, 10, 9, 9, 8, 7, 5, 4, 
            1, 18, 8, 7, 6, 6, 5, 4, 4, 3, 
            3, 2, 11, 6, 6, 5, 5, 4, 3, 2, 2, 1),
  group = c(rep("Tajikistan", 10), rep("Kyrgyzstan", 10), rep("Uzbekistan", 11), 
            rep("Turkmenistan", 11), rep("Kazakhstan", 10))
)

# Add empty bars
empty_bar <- 3
to_add <- data.frame(matrix(NA, empty_bar * nlevels(as.factor(data$group)), ncol(data)))
colnames(to_add) <- colnames(data)
to_add$group <- rep(levels(as.factor(data$group)), each = empty_bar)
data <- rbind(data, to_add)
data <- data %>% arrange(group)
data$id <- seq(1, nrow(data))

# Label data preparation 
label_data <- data
number_of_bar <- nrow(label_data)
angle <- 90 - 360 * (label_data$id - 0.5) / number_of_bar
label_data$hjust <- ifelse(angle < -90, 1, 0)
label_data$angle <- ifelse(angle < -90, angle + 180, angle)

# Base data for grouping
base_data <- data %>%
  group_by(group) %>%
  summarize(start = min(id), end = max(id) - empty_bar) %>%
  rowwise() %>%
  mutate(title = mean(c(start, end)))

# Grid data for scale lines
grid_data <- base_data
grid_data$end <- grid_data$end[c(nrow(grid_data), 1:nrow(grid_data) - 1)] + 1
grid_data$start <- grid_data$start - 1
grid_data <- grid_data[-1, ]

p <- ggplot(data, aes(x = as.factor(id), y = value, fill = group)) +
  geom_bar(stat = "identity", alpha = 0.5, fill = "black") +
  
  # Grid lines
  geom_segment(data = grid_data, aes(x = end, y = 100, xend = start, yend = 100), 
               colour = "black", size = 0.3, inherit.aes = FALSE) +
  geom_segment(data = grid_data, aes(x = end, y = 80, xend = start, yend = 80), 
               colour = "black", size = 0.3, inherit.aes = FALSE) +
  geom_segment(data = grid_data, aes(x = end, y = 60, xend = start, yend = 60), 
               colour = "black", size = 0.3, inherit.aes = FALSE) +
  geom_segment(data = grid_data, aes(x = end, y = 40, xend = start, yend = 40), 
               colour = "black", size = 0.3, inherit.aes = FALSE) +
  geom_segment(data = grid_data, aes(x = end, y = 20, xend = start, yend = 20), 
               colour = "black", size = 0.3, inherit.aes = FALSE) +
  
  
  # Circular bar plot
  ylim(-100, 120) +
  theme_minimal() +
  theme(
    legend.position = "none",
    axis.text = element_blank(),
    axis.title = element_blank(),
    panel.grid = element_blank(),
    plot.margin = unit(rep(-1, 4), "cm")
  ) +
  coord_polar() +
  
  # Labels for individual bars 
  # point label behind in text
  # add point upper bar
  # label point behind in text label
  geom_text(data = label_data, 
            aes(x = id, y = value + 10, label = paste0(individual, " (", value, ")"), hjust = hjust),
            color = "black", fontface = "bold", alpha = 0.8, size = 3, 
            angle = label_data$angle, inherit.aes = FALSE) +
  
  # Base lines and group titles
  geom_segment(data = base_data, 
               aes(x = start, y = -10, xend = end, yend = -10), 
               colour = "black", size = 0.6, inherit.aes = FALSE) +
  geom_text(data = base_data, 
            aes(x = title, y = -40, label = group),  # Turunkan y untuk lebih rapi
            hjust = 0.5,  # Center alignment
            vjust = 0.5,  # Vertikal tengah
            colour = "black", 
            size = 3, fontface = "bold", inherit.aes = FALSE)

# Display the plot
p




#### LDA VISUAL ANALYSIS


library(readxl)
Analysis_frame_Heatmap <- read_excel("Desktop/Reseacrh Immigrant/Analysis_frame_Heatmap.xlsx")
View(Analysis_frame_Heatmap)

library(ggplot2)
ggplot(heatmap, aes(x = Country, y = Framework, fill = `Score Dominant`))+
  geom_tile(colour = "black", linewidth=1.5)+
  scale_fill_gradient(low = "white", high = "black") +
  geom_text(aes(label = round(`Score Dominant`, 2)), color = 'brown4', size = 3) +
  theme_bw() +
  labs(title = "Russian Migration Policy Topics Dominant in the News of Every Central Asian Country",
       subtitle ="By: Latent Dirichlet Allocation (LDA)")+
  theme(plot.title = element_text(face = "bold")) +
  theme(plot.title = element_text(face = "bold", size = 12),
        plot.subtitle = element_text(size = 11),
        plot.caption = element_text(size = 10, hjust = 0)) +
  theme(plot.margin = margin(t = 10, r = 10, b = 10, l = 10))





### SANKEY VISUAL


# Data frame: Frameworks relation narrative

sankey_data <- data.frame(
  source = c("Safety", "Safety", "Public Sentiment", "Public Sentiment", 
             "Justice Equality", "Quality Life", "External Regulator", 
             "External Regulator", "Capacity & Resource"),
  target = c("Political Implication", "Crime & Punishment", 
             "Safety", "Crime & Punishment", 
             "Political Implication", "Economy", 
             "Political Implication", "Crime & Punishment", 
             "External Regulator"),
  value = c(1, 1, 1, 1, 1, 1, 1, 1, 1)  # Set semua bobot menjadi 1
)

# Load library
library(networkD3)


nodes <- data.frame(name = unique(c(sankey_data$source, sankey_data$target)))

# add ID numeric ke source & target
sankey_data$source_id <- match(sankey_data$source, nodes$name) - 1  # ID dimulai dari 0
sankey_data$target_id <- match(sankey_data$target, nodes$name) - 1

# creatw Sankey Diagram
sankey <- sankeyNetwork(
  Links = sankey_data, 
  Nodes = nodes, 
  Source = "source_id", 
  Target = "target_id", 
  Value = "value", 
  NodeID = "name", 
  fontSize = 14, 
  nodeWidth = 20
)

# show diagram
sankey





##### VISUAL SCETTER PLOT


library(readxl)
data <-read_excel()

library(ggplot2)
ggplot(data_pol_sub, aes(x = sentimen_vader_transformers, y = subjectivity, color = Country)) +
  geom_point(size = 1.5)+
  scale_color_manual(values = c(
    "Kazakhstan" = "blue",   
    "Kyrgyzstan" = "red",   
    "Tajikistan" = "green",   
    "Turkmenistan" = "yellow", 
    "Uzbekistan" = "black"    
  )) +
  theme_bw() +
  labs(title = "Russian Migration Policy Discourse Central Asia News",
       subtitle ="By Analysis Subjectivity & Polarity")+
  theme(plot.title = element_text(face = "bold")) +
  theme(plot.title = element_text(face = "bold", size = 12),
        plot.subtitle = element_text(size = 11),
        plot.caption = element_text(size = 10, hjust = 0)) +
  theme(plot.margin = margin(t = 10, r = 10, b = 10, l = 10)) +
  geom_vline(xintercept = 0, linetype = "dashed", color = "grey") +  
  geom_hline(yintercept = 0.5, linetype = "dashed", color = "grey") 








