Summary: A networked Chinese Checkers game for GNOME
Name: gchch
Version: 1.9.0
Release: 1
License: GPL
Group: Amusements/Games
URL: http://gchch.sourceforge.net/
Source: http://loban.caltech.edu/gchch/%{name}-%{version}.tar.gz
BuildRequires: libsigc++-devel, gnet2-devel
BuildRequires: gtkmm24-devel, libgnomeuimm26-devel, libgnomecanvasmm26-devel, libglademm24-devel, gconfmm26-devel
BuildRequires: w3m, udisks2

%description
Gnome Chinese Checkers is an implementation of the Chinese Checkers board
game. It includes a server that can support upto 6 players, all of whom
connect from their own clients. The game includes added goodies like an
integrated chat window, automatic player rotation, computer bots, and more.
This game is dedicated to Nadia Haq, a good friend with whom I've wasted
away countless hours playing board games like this.

%prep
%setup -q
sed -i -e 's|gtkmm-2.0|gtkmm-2.4|' -e 's|libgnomeuimm-2.0|libgnomeuimm-2.6|' -e 's|libgnomecanvasmm-2.0|libgnomecanvasmm-2.6|' -e 's|libglademm-2.0|libglademm-2.4|' -e 's|gconfmm-2.0|gconfmm-2.6|' -e 's|gnet|gnet-2.0|' configure
#sed -i -e 's|SigC::Object|sigc::trackable|g' -e 's|SigC|sigc|g' src/CommonGarbage.*
#sed -i -e 's|slot|sigc::mem_fun|g' src/CommonGarbage.cc
sed -i -e 's|sigc++/|sigc++-1.2/sigc++/|' src/*
sed -i -e 's|GCHCH_CFLAGS=|GCHCH_CFLAGS="-I%{_libdir}/sigc++-1.2/include -I%{_includedir}/sigc++-1.2 "|' configure

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# Remove scrollkeeper generated files to prevent unpackaged file warnings
/bin/rm -rf $RPM_BUILD_ROOT/var/scrollkeeper

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
SCHEMAS="gchch.schemas"
for S in $SCHEMAS; do
	gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/$S  &>/dev/null
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_libdir}/menu/%{name}.menu
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}
%doc %{_datadir}/gnome/help/%{name}
%doc AUTHORS BUGS ChangeLog NEWS NOTES README TODO
%config %{_sysconfdir}/gconf/schemas/*

%changelog
* Sun May 05 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.0
- Rebuild for Fedora
* Tue Mar 04 2003 Loban Rahman <loban@earthling.net> - 1.9.0
- Initial package
