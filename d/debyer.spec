Name:           debyer
Version:        0.2
Release:        10.1
Summary:        A tool for calculation of diffraction patterns for atomistic models
BuildRequires:  gcc-c++
Group:          Applications/Egnineering
License:        GPLv2+
URL:            https://www.unipress.waw.pl/debyer/
Source0:        https://www.unipress.waw.pl/debyer/files/%{name}-%{version}.tar.gz

%description
Debyer is software for calculation of diffraction patterns and PDFs
from a set of atomic positions. 

Typically, the atomic positions are:
- the result of molecular dynamics or other simulations, 
- or simply a geometrical model of investigated structure (i.e. just positions
  are generated, no interactions or time evolution -- such modeling is 
  sometimes used in analysis of experimental diffraction data).

Even tens of millions of atoms can be handled.

%prep
%setup -q
sed -i -e 's/char \*eq/const char *eq/' -e 's/char \*e\[/const char *e[/' -e 's/char \*ptr = e/const char *ptr = e/' debyer/fileio.cc

%build
export CXXFLAGS="%{optflags} -std=c++98 -fPIC"
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files 
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/%{name}
%{_bindir}/dbr*
%{_bindir}/sic*

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora

* Sun Apr 19 2009 Fabian Affolter <fabian@bernewireless.net> - 0.2-1
- Initial package for Fedora
