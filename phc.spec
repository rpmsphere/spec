Summary: PHP compiler
Name: phc
Version: 0.3.0.1git
Release: 1
License: BSD
Group: Development/Languages
URL: https://github.com/pbiggar/phc
Source: phc-master.zip
BuildRequires: flex, bison, gcc-c++, boost-devel, gc-devel, php-cli, php-devel

%description
phc is a compiler for PHP that will translate PHP code directly into Linux
assembly code. It can be used as a (C++) framework for developing refactoring
tools, aspect weavers, script obfuscators, and any other tools that operate
on PHP scripts.

%prep
%setup -q -n phc-master
#sed -i 's|insert(|this->insert(|' src/lib/List.h
#sed -i '1i #include <boost/graph/adjacency_list.hpp>' src/lib/List.h
sed -i 's|error_t|int|' libltdl/argz.h libltdl/ltdl.c
sed -i 's|boost/tr1/unordered_map.hpp|boost/unordered_map.hpp|' src/lib/Map.h

%build
%configure
make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%doc ChangeLog README
%{_bindir}/phc
%{_bindir}/phc_compile_plugin
%{_includedir}/phc
%{_datadir}/phc

%changelog
* Sat Apr 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0.1
- Rebuild for Fedora
* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.7-1 - 4881/dries
- Updated to release 0.1.7
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.5.1-1.2
- Rebuild for Fedora Core 5
* Sat Jan 28 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.5.1-1
- Updated to release 0.1.5.1
* Fri Jan 27 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.5-1
- Updated to release 0.1.5
* Mon Jan 09 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.4-1
- Updated to release 0.1.4
* Mon Dec 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.3-1
- Initial package
