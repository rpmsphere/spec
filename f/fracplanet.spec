%undefine _debugsource_packages

Name: fracplanet
Version: 0.4.0
Release: 6.1
Summary: Application to generate and view random fractal planets and terrain
License: GPL
Group: Applications/Multimedia
URL: https://www.bottlenose.demon.co.uk/share/fracplanet/index.htm
Source: https://nchc.dl.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires: boost-devel libXmu-devel mesa-libGLU-devel qt-devel

%description
fracplanet is an interactive application to generate and view random fractal
planets and terrain with oceans, mountains, icecaps, and rivers, then save
them in POV-Ray format. It uses Qt and OpenGL.

%prep
%setup -q -n %{name}
sed -i '20i #include <GL/glu.h>' triangle_mesh_viewer_display.cpp
sed -i 's|-lboost_program_options|-lboost_program_options -lGLU|' %{name}.pro
sed -i 's|return out;|return bool(out);|' image.cpp

%build
QTDIR=%{_libdir}/qt4 ./BUILD

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 man/man1/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%doc BUGS NEWS THANKS LICENSE README TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Fri Mar 06 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
* Sun Apr 22 2007 Peter Hanecak <hany@hany.sk> 0.3.3-1
- update to 0.3.3
- added %%{?dist} into spec
* Mon Jul 17 2006 Peter Hanecak <hany@hany.sk> 0.3.2-1
- update to 0.3.2
* Sat May 13 2006 Peter Hanecak <hany@hany.sk> 0.3.1-2
- added some missing build requires
* Wed Apr 12 2006 Peter Hanecak <hany@hany.sk> 0.3.1-1
- update to 0.3.1
* Sat Apr  8 2006 Peter Hanecak <hany@hany.sk> 0.3.0-1
- update to 0.3.0
* Fri Aug 19 2005 Peter Hanecak <hanecak@megaloman.sk> 0.2.0-1
- update to 0.2.0
* Mon Jul 14 2003 Peter Hanecak <hanecak@megaloman.sk> 0.0.1-1
- initial spec
