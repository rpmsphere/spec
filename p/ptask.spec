Summary:	A GTK+ graphical user interface for managing tasks
Name:		ptask
Version:	1.0.0
Release:	3.1
URL:		http://wpitchoune.net/blog/ptask/
License:	GNU General Public License version 2
Group:		Applications/Productivity
Source0:	http://wpitchoune.net/ptask/files/%{name}-%{version}.tar.gz
Requires:	task
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: gtk3-devel
BuildRequires: json-c-devel

%description
ptask is based on taskwarrior, a well-known and robust command line tasks manager.
Unlike taskwarrior, it is possible to associate a note (long description) to each task.

%prep
%setup -q
sed -i 's|is_error(o)|o==NULL|' src/tw.c

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/doc/%{name}
%{_datadir}/glib-2.0/schemas/%{name}.gschema.xml
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/man/man1/%{name}*.1.*
%{_datadir}/icons/*/*/*/%{name}*
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Jul 12 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuilt for Fedora
