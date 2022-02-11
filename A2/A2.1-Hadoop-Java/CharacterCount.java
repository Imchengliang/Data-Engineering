import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class CharacterCount {
	public static class CharacterCountMapper
		extends Mapper<LongWritable, Text, Text, IntWritable> {

		@Override
		public void map(LongWritable key, Text value, Context context) 
			throws IOException, InterruptedException {
			String line = value.toString().toLowerCase();
			String[] strings = line. split(" ");

			for(int i=0; i<strings.length; i++) {
				if ( strings[i] != null && !strings[i].isEmpty() ){
					char firstLetter = strings[i].charAt(0);
    					if (firstLetter >= 'a' && firstLetter <= 'z') {
        					context.write(new Text(String.valueOf(firstLetter)), new IntWritable(1));
					}
    				}
                        }

		}
	} 

	public static class CharacterCountReducer
			extends Reducer<Text, IntWritable, Text, IntWritable> {

		private IntWritable result = new IntWritable();

		@Override
		public void reduce(Text key, Iterable<IntWritable> values, Context context)  
			throws IOException, InterruptedException {

			int sum = 0;
			for (IntWritable val : values) {
				sum += val.get();

         }
			result.set(sum);
			context.write(key, result);

   	}
	}

	public static void main(String[] args) throws Exception {

		if (args.length != 2){
			System.err.println("Err: CharacterCount requires <input path> <output path>");
			System.exit(-1);
		}

		Configuration conf = new Configuration();
		Job job = new Job(conf);
		job.setJarByClass(CharacterCount.class);
		job.setJobName("CountCharacter Job");

		FileInputFormat.addInputPath(job, new Path(args[0]));
    	FileOutputFormat.setOutputPath(job, new Path(args[1]));

    	job.setMapperClass(CharacterCountMapper.class);
    	job.setCombinerClass(CharacterCountReducer.class);
    	job.setReducerClass(CharacterCountReducer.class);

    	job.setOutputKeyClass(Text.class);
    	job.setOutputValueClass(IntWritable.class);
    	
    	System.exit(job.waitForCompletion(true) ? 0 : 1);

	}

}








