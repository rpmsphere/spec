Name:          jikes
Version:       1.22
Release:       5.1
Summary:       A Java compiler
Group:         Development/Libraries/Java
URL:           http://jikes.sourceforge.net/
Source:        http://downloads.sourceforge.net/jikes/jikes-%{version}.tar.bz2
License:       IBM Public license
BuildRequires: gcc-c++

%description
JikesTM is a compiler that translates JavaTM source files as defined in The
Java Language Specification into the bytecoded instruction set and binary
format defined in The Java Virtual Machine Specification.

%prep
%setup -q

%build
autoreconf -ifv

./configure \
   --prefix=%{_prefix} \
   --mandir=%{_mandir}
make %{_smp_mflags}

%install
rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/jikes
%{_includedir}/*.h
%{_datadir}/doc/jikes-%{version}/license.htm
%{_mandir}/*

%changelog
* Wed Jun 15 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.22
- Rebuild for Fedora
* Tue Jul 08 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 1.22-2mamba
- fixed license
- fixed specfile formatting
- added automatic build requirements
* Wed Sep 26 2007 Fabio Giani <fabio.giani@email.it> 1.22-1mamba
- update to 1.22
* Thu May 13 2004 Silvan Calarco <silvan.calarco@qilinux.it> 2.5r2-1qilnx
- first build
