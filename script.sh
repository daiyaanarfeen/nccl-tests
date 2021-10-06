for nnode in {1..8}; do
  for nproc in {1..8}; do
    for iter in {1..20}; do
      NCCL_ALGO=ring mpirun --hosts phortx1:$nproc,phortx2:$nnode ./build/all_reduce_perf -b 1M -e 16M -f 2 -g 1 -n 1 -w 20 -z 1\
        | grep float | awk '{gsub(/[ ]+/,",")}1' > output.csv && \
	python process_csv.py --nproc $((nproc+nnode)) --nnode $((nproc > nnode ? nproc : nnode));
    done;
  done;
done
