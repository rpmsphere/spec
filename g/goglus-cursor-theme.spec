Name:           goglus-cursor-theme
Version:        1
Release:        4.1
Summary:        Goglus X11 Mouse Cursor theme
Group:          System/X11/Icons
License:        BSD
URL:            https://gnome-look.org/content/show.php/goglus_cursor?content=127487
Source0:        127487-goglus_cursor.tar.gz
BuildArch:      noarch

%description
Goglus mouse cursor theme for X11 system.

%prep
%setup -q -n goglus_cursor

%build

%install
%__install -D -d -m 755 %{buildroot}%{_datadir}/icons/goglus/cursors
%__install -m 644 cursors/* %{buildroot}%{_datadir}/icons/goglus/cursors
%__install -m 644 index.theme %{buildroot}%{_datadir}/icons/goglus

%files
%doc COPYRIGHT LICENSE
%{_datadir}/icons/goglus

%changelog
* Sun Jan 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora
* Mon Feb  6 2012 nekolayer@yandex.ru
- initial package
