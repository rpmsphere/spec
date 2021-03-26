%global debug_package %{nil}
%define   _base Dudeball
%define   _unstable unstable

Name:           dudeball
Version:        2.3.4
Release:        1
Summary:        A 2D arcade game as soccer
Group:          Amusements/Games
URL:            https://launchpad.net/dudeball
License:        I don't know yet 
Source0:        %{_base}-%{version}_%{_unstable}.tar.gz
Source1:        Makefile.%{name}
Source2:        %{name}.png
Source3:        %{name}.desktop
Source4:        %{name}.sh
Requires:       SDL SDL_image SDL_ttf
BuildRequires:  SDL-devel SDL_image-devel SDL_ttf-devel

%description
Dudeball is a 2D arcade game which is written in C. The rules are damn easy,
almost as in soccer.

%prep
%setup -q -n %{_base}-%{version}
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} .
cp %{SOURCE1} Makefile

%build
%{__make} -i

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.4
- Rebuild for Fedora
* Mon May 22 2012 Chris Lin <chris@ossii.com.tw> 2.3.4-1
- first
