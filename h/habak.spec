%undefine _debugsource_packages

Summary:	"Ha" Background - setting of window manager background image
Name:		habak
Version:	0.2.5
Release:	1
License:	GPL
Group:		Graphical desktop/Other
Source0:	http://fvwm-crystal.berlios.de/files/files/habak/%{name}-%{version}.tar.gz
URL:		http://fvwm-crystal.berlios.de/
BuildRequires:	imlib2-devel

%description
Habak sets window manager background image. Habak uses layered model.
Lowest layer is completely black screen. On this screen you can put
other objects called habaks. There are 3 kinds of habaks: images,
fonts and internals. Wallpaper is made by combining one or more
habaks. Order of defining habaks in command line is also order of
putting it on stack, so habak which is last on the command line is
drawn over all previous habaks.

%prep
%setup -q
sed -i 's|-lm|-lX11 -lm -Wl,--allow-multiple-definition|' src/Makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 habak $RPM_BUILD_ROOT/%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog README TODO
%{_bindir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.5
- Rebuilt for Fedora
* Wed Nov 26 2008 Feather Mountain <john@ossii.com.tw> 0.2.5-1.ossii
- Rebuild for M6(OSSII)
* Tue Mar 11 2008 P. K. Frederic <pkfric@yahoo.com> 0.2.5-1pclos2007
- first RPM for PCLinuxOS
