Name:       oxstcalculator  
Version:        0.1
Release:        5
Summary:        calculator
Group:          Applications/Education
License:        enyo
Source0:        %{name}-%{version}.ox.tgz
Requires:       oxzilla
BuildArch:	noarch
BuildRequires:  oxzilla


%description
這是一款計算機,一定是您的好幫手

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0777,root,root,0777)
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_bindir}/%{name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Mon Jun 11 2012 Simon Sun <simon.sun@ossii.com.tw> 0.1-1 
- Build for first time

