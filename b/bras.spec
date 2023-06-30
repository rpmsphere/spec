Summary:	Rule Based Command Execution
Name:		bras
Version:	2.3.2
Release:	10.1
License:	GPL
Group:		Development/Tools
Source0:	https://download.berlios.de/bras/%{name}-%{version}.tar.gz
URL:		https://bras.berlios.de/
BuildArch:	noarch
BuildRequires:	tcl

%description
Bras helps to keep files, or targets, up-to-date with respect to a set
of dependencies. For every target, a rule describes what it means for
the target to be out-of-date and what has to be done to refresh it.

%prep
%setup -q

%build
tclsh bras prefix=$RPM_BUILD_ROOT/usr

%install
rm -rf $RPM_BUILD_ROOT
tclsh bras install prefix=$RPM_BUILD_ROOT/usr
sed -i 's|%{buildroot}||' $RPM_BUILD_ROOT/usr/bin/%{name} $RPM_BUILD_ROOT/usr/man/man1/%{name}.1 $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}/%{name}.1.html
mkdir -p $RPM_BUILD_ROOT/usr/share
mv $RPM_BUILD_ROOT/usr/doc $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/usr/share
cp README TODO CHANGES ANNOUNCE $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
/usr/lib/%{name}-%{version}
%{_docdir}/%{name}-%{version}
%{_mandir}/man?/*

%changelog
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.2
- Rebuilt for Fedora
