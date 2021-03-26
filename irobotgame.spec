Name:		irobotgame		
Version:	0.7.5
Release:	1
Summary:	Irobot Game	
Group:		Amusements/Games
License:	GPL	
URL: 		http://irobotgame.googlecode.com/		
Source0:	http://irobotgame.googlecode.com/files/irobotgame-0.7.5.tar.gz
Requires:	pyglet
BuildArch:	noarch

%description
irobotgame is a robot dancing game develop for pyweek challenge.

%prep
%setup -q
rm -rf lib/pyglet
sed -i -e '12d' -e 's|libdir|"/usr/share/%{name}/lib"|' run_game.py

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 run_game.py $RPM_BUILD_ROOT%{_bindir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a AUTHORS COPYING data lib LICENSE LICENSE_OTHERS README VERSION $RPM_BUILD_ROOT%{_datadir}/%{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Mon Mar 05 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.5
- Rebuild for Fedora
* Fri Jun 1 2012 johnwu <johnwu@ossii.com.tw>
- First
