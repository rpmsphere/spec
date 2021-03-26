%global debug_package %{nil}
Summary: 	Interactive GCC
Name: 		igcc
Version: 	0.2
Release: 	4.1
License: 	GPL
Group: 		Development/Python
Source: 	http://sourceforge.net/projects/igcc/files/%{name}-%{version}.tar.bz2
URL:		http://www.artificialworlds.net/wiki/IGCC/IGCC
BuildRequires: 	python2-devel
BuildArch: 	noarch

%description 
IGCC is a real-eval-print loop (REPL) simulator for C/C++ programmers.
It allows you to type C++ commands which are immediately compiled and executed.
Underneath it uses the normal GCC exe for compiling.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -d $RPM_BUILD_ROOT%{python2_sitelib}
cp -a lib%{name} $RPM_BUILD_ROOT%{python2_sitelib}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%doc *.txt
%{_bindir}/%{name}
%{python2_sitelib}/*

%changelog
* Sun Sep 30 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
