%undefine _debugsource_packages

Name: avida
Summary: Digital Life Platform
Version: 2.12.4
Release: 13.1
Group: Science/Engineering
License: GPL
URL: http://avida.devosoft.org/
Source0: http://sourceforge.net/projects/%{name}/files/%{name}-stable/%{version}/%{name}-%{version}-src.tar.gz
BuildRequires: gcc-c++
BuildRequires: cmake

%description
Avida is arguably the most advanced software platform to study digital
organisms to date, and is certainly the one that has had the biggest impact
in the biological literature so far. Having reached version 2.12, it now
supports detailed control over experimental settings, a sophisticated system
to design and execute experimental protocols, a multitude of possibilities
for organisms to interact with their environment (including depletable
resources and conversion from one resource into another) and a module to
post-process data from evolution experiments (including tools to find the
line of descent from the original ancestor to any final organism, to carry
out knock-out studies with organisms, to calculate the fitness landscape
around a genotype, and to align and compare organisms’ genomes).

%prep
%setup -q -n %{name}-%{version}-src
sed -i '1i #include <cstdlib>' avida-core/source/tools/tArray.h

%build
export CXXFLAGS="-Wno-error -std=c++98"
cmake .
make %{?_smp_mflags}

%install
make install
install -d %{buildroot}%{_bindir}
install -m755 work/%{name}* %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
install -m755 work/*.org work/*.cfg %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_libdir}
install -m755 libs/apto/lib/* libs/tcmalloc-1.4/lib/* %{buildroot}%{_libdir}

%files
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_libdir}/lib*

%changelog
* Sun Jan 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.12.4
- Rebuilt for Fedora
