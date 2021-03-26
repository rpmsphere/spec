Name: codonphyml
Summary: Markovian codon models of evolution in phylogeny reconstruction
Version: 1.00.201304.11
Release: 10.1
Group: Applications/Engineering
License: GPLv3
URL: http://sourceforge.net/projects/codonphyml
Source0: http://jaist.dl.sourceforge.net/project/codonphyml/codonPhyML_dev_1.00_201304.11.zip
BuildRequires: automake

%description
Given a set of species characterized by their DNA sequences as input,
codonPhyML will return the phylogenetic tree that best describes their
evolutionary relationship. Our paper describing codonPhyML has been
accepted for publication in the journal "Molecular Biology and Evolution".

%prep
%setup -q -n codonPHYML_dev

%build
autoreconf -f -i
automake --add-missing
autoconf
%configure
make %{?_smp_mflags} CFLAGS+="-fPIC"

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}

%changelog
* Sun May 05 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.00.201304.11
- Rebuild for Fedora
