%global __os_install_post %{nil}
%undefine _debugsource_packages

Summary: Dao Programming Language
Name: dao
Version: 2.0beta
Release: 1
License: MIT
Group: Development/Languages
Source: https://github.com/daokoder/dao/archive/master.zip#/%{name}-master.zip
URL: https://daoscript.org/

%description
Dao is a lightweight and optionally typed programming language
with many interesting features. It includes features that can
make concurrent programming much simpler. It has well designed
interfaces for easy embedding and extending.

%prep
%setup -q -n %{name}-master

%build
make -f Makefile.daomake linux

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL=%{buildroot}/usr

%files 
%doc ChangeLog README *.txt
%{_bindir}/%{name}*
%{_includedir}/%{name}
/usr/lib/%{name}*
/usr/lib/lib%{name}*
%{_datadir}/%{name}

%changelog
* Fri Sep 27 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0beta
- Rebuilt for Fedora
