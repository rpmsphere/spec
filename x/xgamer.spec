Name: xgamer
Summary: A launcher for starting games in a second X session
Version: 0.6.2
Release: 8.1
Group: Amusements/Games
License: GPLv3
URL: https://code.google.com/p/xgamer/
Source0: https://xgamer.googlecode.com/files/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: perl-Module-Build, perl-JSON-PP

%description
XGamer is a launcher for starting games or applications in a second X11 session.
It can be launched from the command line or has a Gtk2 GUI for managing and
launching games. It has integration with openbox (a light-weight window manager)
to provide a suitable environment for running processor or graphics intensive
applications.

By running in a second session games can run at the same time as compositing
programs such as Compiz in your main session. It It also isolates your primary
X11 session from unstable games and applications preventing bugs or crashes
propagating to other applications. Running a second session can also take
advantage of multi-core processors.

%prep
%setup -q -n %{name}
sed -i '6i use lib q[.];' Build.PL

%build
perl Build.PL --prefix %{buildroot}/usr
./Build

%install
./Build install

%files
%doc COPYING README
%{_bindir}/xgamer
%{_libdir}/perl5/*/auto/App/XGamer/.packlist
%{_datadir}/applications/xgamer.desktop
%{_datadir}/man/man1/xgamer.1.*
%{_datadir}/pixmaps/xgamer.png
%{_datadir}/%{name}

%changelog
* Sun May 26 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.2
- Rebuild for Fedora
