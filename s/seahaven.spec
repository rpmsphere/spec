%undefine _debugsource_packages
Name:            seahaven  
Version:         1.60
Release:         1
Summary:         Solitaire card game
Group:           Amusements/Games
License:         GPL
URL:             https://seahaven.sourceforge.net/
Source0:         https://seahaven.sourceforge.net/%{name}-%{version}.tgz
Source1:         %{name}.desktop
Source2:         %{name}.png
BuildRequires:   gcc-c++ libXft-devel libXext-devel

%description
This is Seahaven Towers, a solitaire card game written for X11R4 and C++. 
With this program you can waste great amounts of time. 

%prep
%setup -q

%build
export CPPFLAGS=-Wno-narrowing
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man6/
install -m 644 %{name}.6 %{buildroot}%{_mandir}/man6/
install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man?/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.60
- Rebuilt for Fedora
* Wed Oct 31 2012 Simon Sun <simon.sun@ossii.com.tw> 1.60-1
- First build
