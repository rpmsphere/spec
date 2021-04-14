Summary:	System monitor
Name:		sentinella
Version:	0.9.0
Release:	10.4
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://sentinella.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/0.9.x/%{name}-%version.tar.xz
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	qt4-devel
BuildRequires:	libsysactivity-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kde-workspace-devel
BuildRequires:	qca2 udisks2

%description
Application that monitors your system activity and, when a condition is met,
takes the action that you've chosen.
While monitoring your CPU, memory, hard drive and network usage, Sentinella
can be programmed to take specific actions when set-points for utilization
or time are met. It can power off, reboot or hibernate your system,
kill an active process, throw an alarm or execute any command.

%prep
%setup -q

%build
%cmake 
make

%install
%make_install
%find_lang %{name} --with-kde
desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="X-MandrivaLinux-System-Monitoring" \
	--dir %{buildroot}%{_datadir}/applications/kde4/ \
	%{buildroot}%{_datadir}/applications/kde4/*

%files -f %{name}.lang
%doc CHANGELOG COPYING
%{_bindir}/sentinella
%{_datadir}/applications/kde4/%{name}.desktop
%{_datadir}/sounds/Sentinella
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0
- Rebuilt for Fedora
* Tue May 29 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.9.0-1
+ Revision: 801027
- imported package sentinella
