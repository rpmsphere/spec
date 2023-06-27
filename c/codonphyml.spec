Name: codonphyml
Summary: Markovian codon models of evolution in phylogeny reconstruction
Version: 1.00.201407.24
Release: 1
Group: Applications/Engineering
License: GPLv3
URL: https://sourceforge.net/projects/codonphyml
Source0: https://jaist.dl.sourceforge.net/project/codonphyml/codonPhyML_dev_1.00_201407.24.zip
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
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.00.201407.24
- Rebuilt for Fedora
