%undefine _debugsource_packages

Name: qiime
Summary: Quantitative Insights Into Microbial Ecology
Version: 1.9.0
Release: 0.rc1
Group: science
License: Free Software
URL: https://www.qiime.org/
Source0: %{name}-%{version}-rc1.tar.gz
BuildRequires: python2-devel
BuildRequires: python2-setuptools
#Requires: libffi6
#Requires: libgmp10,
#Requires: pynast
#Requires: python-cogent
#Requires: king,
#Requires: python-biom-format
#Requires: fasttree,
#Requires: python-qcli,
#Requires: libjs-jquery,
#Requires: python-matplotlib,
#Requires: python-numpy
#Conflicts: denoiser
Provides: denoiser

%description
QIIME (canonically pronounced ‘Chime’) is a pipeline for performing
microbial community analysis that integrates many third party tools which
have become standard in the field. A standard QIIME analysis begins with
sequence data from one or more sequencing platforms, including
 * Sanger,
 * Roche/454, and
 * Illumina GAIIx.
With all the underlying tools installed,
of which not all are yet available in Debian (or any other Linux
distribution), QIIME can perform
 * library de-multiplexing and quality filtering;
 * denoising with PyroNoise;
 * OTU and representative set picking with uclust, cdhit, mothur, BLAST,
   or other tools;
 * taxonomy assignment with BLAST or the RDP classifier;
 * sequence alignment with PyNAST, muscle, infernal, or other tools;
 * phylogeny reconstruction with FastTree, raxml, clearcut, or other tools;
 * alpha diversity and rarefaction, including visualization of results,
   using over 20 metrics including Phylogenetic Diversity, chao1, and
   observed species;
 * beta diversity and rarefaction, including visualization of results,
   using over 25 metrics including weighted and unweighted UniFrac,
   Euclidean distance, and Bray-Curtis;
 * summarization and visualization of taxonomic composition of samples
   using pie charts and histograms
and many other features.

QIIME includes parallelization capabilities for many of the
computationally intensive steps. By default, these are configured to
utilize a mutli-core environment, and are easily configured to run in
a cluster environment. QIIME is built in Python using the open-source
PyCogent toolkit. It makes extensive use of unit tests, and is highly
modular to facilitate custom analyses.

%prep
%setup -q -n %{name}-%{version}-rc1

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --prefix=/usr --skip-build

%files
%doc *.md COPYING.txt
#%{_sysconfdir}/%{name}/
%{_bindir}/*
%{python2_sitelib}/%{name}*
#%{_libdir}/%{name}/
#%{_datadir}/pyshared/%{name}/
#%{_datadir}/python/runtime.d/%{name}.rtupdate
#%{_datadir}/%{name}/

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.0-rc1
- Rebuilt for Fedora
