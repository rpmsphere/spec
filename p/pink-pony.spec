Name:		pink-pony		
Version:	1.2.1
Release:	1
Summary:	A Tron-like multiplayer racing­game	
Group:		Amusements/Games
License:	GPL	
URL: 		http://code.google.com/p/pink-pony/		
Source0:	http://code.google.com/p/pink-pony/downloads/%{name}-%{version}.tar.bz2
Source1:	%{name}-SConstruct
BuildRequires:	scons
BuildRequires:	libglfw-devel
BuildRequires:	ilmbase-devel
BuildRequires:	DevIL-devel
BuildRequires:	protobuf-devel
BuildRequires:	audiere-devel
BuildRequires:	ftgl-devel
BuildRequires:	libsigc++20-devel
BuildRequires:  DevIL-ILUT-devel
BuildRequires:  tinyxml-devel

%description
You control little ponies that leave a trail of flowers everywhere they step.
You have to evade these trails and force other ponies into them. The last pony
standing wins the game.

%prep
%setup -q 
cp %{SOURCE1} SConstruct

%build
scons

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a README GLSL fonts levels models music textures pony.options level.xml Pony $RPM_BUILD_ROOT%{_datadir}/%{name}
install -Dm755 install/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 install/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 install/%{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Jun 1 2012 johnwu <johnwu@ossii.com.tw>
- First
