# ga4gh-http1.1-streaming
Quick CherryPy app to benchmark streaming performance on HTTP/1.1 using chunked transfer encoding.


## Get it

```
git clone git@github.com:andrewjesaitis/ga4gh-http1.1-streaming.git
cd ga4gh-http1.1-streaming
pip install -r requirements.txt
```

## Back it

```
cd ga4gh-http1.1-streaming/data/release
wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr1.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz
wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr1.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz.tbi
```

## Run it

```
python server.py
<open another terminal>
curl -v localhost:8080/variantsearch
```
