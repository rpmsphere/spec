%global debug_package %{nil}

Name:		QTeXEngine
Version:	0.3
Release:	6.1
Summary:	Library enabling Qt based applications to easily export graphics to TeX
License:	GPLv3
Group:		System Environment/Libraries
URL:		http://soft.proindependent.com/qtexengine/
Source0:	http://download.berlios.de/qtiplot/%{name}-%{version}-opensource.zip
# Fixes the build and install of QTeXEngine
Patch0:		QTeXEngine-svn1552-path.patch
BuildRequires:	qt4-devel doxygen dos2unix

%description
QTeXEngine is a library enabling Qt based applications to easily export
graphics created using the QPainter class to TeX. It is built on top of
QPaintEngine and uses the TikZ/Pgf graphic systems for TeX.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	qt4-devel%{?_isa}
Obsoletes:	%{name}-doc < 0.2-3.20100119svn

%description devel
The %{name}-devel package contains library, header file and documentation
for developing applications that use %{name}.

%prep
%setup -q -n %{name}
%patch0 -p1

rm -rf {example,test}/.svn

# Remove DOS line endings
dos2unix -k *.txt
dos2unix -k example/*
dos2unix -k src/*

# Remove exec permission
find -type f -exec chmod 0644 {} ";"

%build
export PATH=%{_qt4_bindir}:$PATH
pushd src
%{_qt4_qmake} CONFIG+=" QTeXEngineDll" LIBDIR=%{_libdir}
popd
make %{?_smp_mflags} -C src

pushd doc
doxygen Doxyfile
# Fix the time stamp
for file in html/*; do
	touch -r Doxyfile $file
done
popd

%install
make install INSTALL="install -p" INSTALL_ROOT=%{buildroot} -C src

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc *.txt
%{_libdir}/libQTeXEngine.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/html example
%{_includedir}/QTeXEngine.h
%{_libdir}/libQTeXEngine.so

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Tue Nov 30 2010 Chen Lei <supercyper@163.com> - 0.3-1
- Update to 0.3
* Fri Sep 10 2010 Chen Lei <supercyper@163.com> - 0.2-4.20100119svn
- move header file to %%{_includedir}
* Fri Jul 09 2010 Chen Lei <supercyper@163.com> - 0.2-3.20100119svn
- add missing BR: qt4-devel
* Sat Jan 23 2010 Chen Lei <supercyper@163.com> - 0.2-2.20100119svn
- svn 1552
- split doc subpackage
* Thu Jan 21 2010 Chen Lei <supercyper@163.com> - 0.2-1
- use qt4-based rpm macros
- drop Requires(post,postun)
* Sun Nov 29 2009 Chen Lei <supercyper@163.com> - 0.2-0
- initial rpm build
