echo "*** Start of job ***"
date
echo ""

python3 -m nmt.nmt \
  --out_dir=$(PWD)/tmp/nmt_model/opencc \
  --inference_input_file=$(PWD)/infer.txt \
  --inference_output_file=$(PWD)/infer_results/infer_opencc.txt

echo ""
date
echo "*** End of job ***"
