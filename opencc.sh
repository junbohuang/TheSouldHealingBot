#!/bin/bash

python3 -m nmt.nmt \
    --src=q --tgt=a \
    --vocab_prefix=$(PWD)/tmp/nmt_data/opencc/vocab  \
    --train_prefix=$(PWD)/tmp/nmt_data/opencc/train \
    --dev_prefix=$(PWD)/tmp/nmt_data/opencc/val  \
    --test_prefix=$(PWD)/tmp/nmt_data/opencc/test \
    --out_dir=$(PWD)/tmp/nmt_model/opencc/ \
    --num_train_steps=12000 \
    --steps_per_stats=100 \
    --num_layers=1 \
    --num_units=256 \
    --dropout=0.2 \
    --metrics=bleu\
    --residual=False\
    --batch_size=56\
    --optimizer='adam'\
    --learning_rate=0.0001

echo ""
date
echo "*** End of SGE job ***"
