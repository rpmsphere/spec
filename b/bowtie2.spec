Name:		bowtie2
Version:	2.3.5.1
Release:	1
Summary:	Fast and sensitive read alignment
License:	GPLv3+
URL:		http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
Source0:	http://downloads.sourceforge.net/bowtie-bio/%{name}/%{version}/%{name}-%{version}-source.zip
Patch1:		bowtie2-tinythread.patch
BuildRequires:	gcc-c++ libtinythread++-devel

%description
Bowtie 2 is an ultrafast and memory-efficient tool for aligning
sequencing reads to long reference sequences. It is particularly good
at aligning reads of about 50 up to 100s or 1,000s of characters, and
particularly good at aligning to relatively long (e.g. mammalian)
genomes. Bowtie 2 indexes the genome with an FM Index to keep its
memory footprint small: for the human genome, its memory footprint is
typically around 3.2 GB. Bowtie 2 supports gapped, local, and
paired-end alignment modes.
Please cite:
Langmead B, Salzberg S. Fast gapped-read alignment with Bowtie 2.
Nature Methods. 2012, 9:357-359

%prep
%setup -q
# tinythread is unbundled
rm fast_mutex.h tinythread.*
# cpuid.h is in gcc
rm -r third_party
#patch1 -p1 -b .tinythread
chmod +x example/reads/simulate.pl
%ifarch %ix86
sed -i 's|\$(error bowtie2 compilation requires a 64-bit platform )|BITS=32|' Makefile
sed -i 's|64|32|' Makefile
%endif
sed -i 's|“|"|' processor_support.h

%build
make %{?_smp_mflags} EXTRA_FLAGS="%{optflags}" BUILD_LIBS=-ltinythread++ \
     SEARCH_LIBS=-ltinythread++ BITS=64

%install
rm -rf %{buildroot}
make install DESTDIR=%buildroot prefix=%_prefix
mkdir -p %{buildroot}/%_datadir/%name
cp -a example scripts %{buildroot}/%{_datadir}/%name/
ln -s bowtie2-align-s %{buildroot}/%_bindir/bowtie2-align
chmod 755 example/reads/simulate.pl

sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files
%doc doc/{style.css,manual.html} AUTHORS LICENSE NEWS MANUAL TUTORIAL
%{_bindir}/*
%{_datadir}/%name

%changelog
* Tue Oct 01 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.5.1
- Rebuilt for Fedora
* Thu Jan 14 2016 Dave Love <loveshack@fedoraproject.org> - 2.2.6-1
- New version
- Modify patch
- Use make install target
- Don't link the -build and -inspect programs
- Restrict to x86 (for -msse2)
* Mon Mar 30 2015 Dave Love <d.love@liverpool.ac.uk> - 2.2.5-1
- New version
* Mon Dec  1 2014 Dave Love <d.love@liverpool.ac.uk> - 2.2.4-1
- New version
* Wed Jun  4 2014 Dave Love <d.love@liverpool.ac.uk> - 2.2.3-1
- Update to 2.2.3
- Use unbundled libtinythread++ and cpuid.h
- Only for 64-bit architectures
- Obsolete bowtie 1 (bowtie- binaries are included)
- Make compatibility links to small versions
* Wed Jun  4 2014 Dave Love <d.love@liverpool.ac.uk> - 2.1.0-3
- Use unbindled libtinythread++, remove bundled cpuid.h
* Wed Nov 20 2013 Dave Love <d.love@liverpool.ac.uk> - 2.1.0-2
- Include the scripts directory and don't include doc/README
- Note tinythread licence
* Sun May 12 2013 Dave Love <d.love@liverpool.ac.uk> - 2.1.0-1
- Initial version, based on bowtie
