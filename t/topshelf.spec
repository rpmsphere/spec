Name:           topshelf
Version:        0.3.1
Release:        1
Summary:        Current files applet for GNOME
Group:          User Interface/Desktops
License:        GPLv2
URL:            https://launchpad.net/topshelf
Source0:        https://launchpadlibrarian.net/11639150/%{name}-%{version}.tar.gz
Requires:       libgnome, pygtk2
BuildArch:	noarch

%description
TopShelf is a simple GNOME applet which provides a place to store the files
the user is currently working on (not right now, but in general, in a period
of time). Unlike a real shelf, however, TopShelf just links to the files;
it doesn't contain them.

The concept of TopShelf is to contain files that are put there by the user,
as opposed to the 'recent files list' which is automatically managed.
For example, the top shelf might contain a story the user is currently writing;
a project for school or for work, a diary, etc. On the other hand, music and
video files would typically not be in the top shelf (since they cycle very fast),
but they would appear in the recent files list.

%prep
%setup -q
sed -i "s/pixmaps/topshelf/g" topshelf.py
sed -i "s/topshelf-48.png/topshelf.png/g" topshelf.server

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm644 %{name}.server $RPM_BUILD_ROOT/usr/lib/bonobo/servers/%{name}.server
install -Dm755 %{name}.py $RPM_BUILD_ROOT/usr/lib/gnome-panel/%{name}.py
install -Dm644 %{name}-48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp %{name}-24*.png %{name}-svg*.svg $RPM_BUILD_ROOT%{_datadir}/%{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}/usr/lib/gnome-panel/topshelf.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING %{name}.docbook
/usr/lib/bonobo/servers/%{name}.server
/usr/lib/gnome-panel/%{name}.py*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
