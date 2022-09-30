Name: mira-assembler
Summary: Whole Genome Shotgun and EST Sequence Assembler
Version: 4.9.6
Release: 1
Group: science
License: Free Software
URL: http://chevreux.org/projects_mira.html
Source0: mira-%{version}.tar.bz2
BuildRequires: gcc-c++ automake
BuildRequires: boost-devel
BuildRequires: vim-common
#Requires: libexpat1
#Requires: libtcmalloc-minimal4,
#Requires: zlib1g

%description
The mira genome fragment assembler is a specialised assembler for
sequencing projects classified as 'hard' due to high number of similar
repeats. For expressed sequence tags (ESTs) transcripts, miraEST is
specialised on reconstructing pristine mRNA transcripts while
detecting and classifying single nucleotide polymorphisms (SNP)
occuring in different variations thereof.

The assembler is routinely used for such various tasks as mutation
detection in different cell types, similarity analysis of transcripts
between organisms, and pristine assembly of sequences from various
sources for oligo design in clinical microarray experiments.

The package provides the following executables:
Binaries provided:
 * mira: for assembly of genome sequences
 * miramem: estimating memory needed to assemble projects. Realised through
   link to mira.
 * convert_project: for converting project file types into other types
 * caf2fasta, caf2gbf, caf2text, caf2html, gbf2caf and gbf2fasta are some
   frequently used file converters (realised through links to convert_project)
 * scftool: set of tools useful when working with SCF trace files
 * fastatool: set of tools useful when working with FASTA trace files

Scripts provided:
 * fasta2frag: fragmenting sequences into smaller, overlapping
   subsequences. Useful for simulating shotgun sequences. Can create
   subsequences in both directions (/default) and also paired-end sequences.
 * fastaselect: given a FASTA file (and possibly a FASTA quality file) and
   a file with names of reads, select the sequences from the input FASTA (and
   quality file) and writes them to an output FASTA
 * fastqselect: like fastaselect, only for FASTQ
 * fixACE4consed: Consed has a bug which incapacitates it from reading
   consensus tags in ACE files written by the MIRA assembler (and possibly
   other programs). This script massages an ACE file so that consed can read
   the consensus tags.

%prep
%setup -q -n mira-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/fasta2frag
%{_bindir}/fixACE4consed
%{_bindir}/mira
%{_bindir}/mirabait
%{_bindir}/miraconvert
%{_bindir}/miramem
%{_datadir}/doc/%{name}/
%{_datadir}/lintian/overrides/%{name}
%{_mandir}/man1/convert_project.1.gz
%{_mandir}/man1/fasta2frag.1.gz
%{_mandir}/man1/fastaselect.1.gz
%{_mandir}/man1/fastatool.1.gz
%{_mandir}/man1/fastqselect.1.gz
%{_mandir}/man1/fixACE4consed.1.gz
%{_mandir}/man1/mira.1.gz
%{_mandir}/man1/miraSearchESTSNPs.1.gz
%{_mandir}/man1/mirabait.1.gz
%{_mandir}/man1/miradiff.1.gz
%{_mandir}/man1/miramem.1.gz
%{_mandir}/man1/miramer.1.gz
%{_mandir}/man1/scftool.1.gz
%{_datadir}/mira/demoparam.prm
%{_datadir}/mira/support_3rdparty_tools/GTAGDB
%{_datadir}/mira/support_3rdparty_tools/README
%{_datadir}/mira/support_3rdparty_tools/consedrc.13.0
%{_datadir}/mira/support_3rdparty_tools/consedtaglib.txt

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 4.9.6
- Rebuilt for Fedora
