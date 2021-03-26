Name:           gtk-lighthouseblue-engine
Version:        2.7.5
Release:        7.1
Summary:        LighthouseBlue GTK Theme Engine
License:        GPL
URL:            https://www.gnome-look.org/p/1014625/
Group:          System/GUI/GNOME
Source0:        https://dl.opendesktop.org/api/files/download/id/1460763294/137266-gtk-engines-lighthouseblue-%{version}-eq3.tar.gz
BuildRequires:  gtk2-devel

%description
This is the LighthouseBlue GTK2 Engine that was removed in the 2.8.x releases
of gtk-engines. I took a GIT snapshot of the tree right before the engine was
removed, made a few modifications, and stripped the tarball down to the bare-
bones, so it won\'t clobber your more up-to-date GTK engines when you install it.

%prep
%setup -q -n gtk-engines-lighthouseblue-%{version}-eq1.2

%build
%configure
make

%install
%make_install

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING.GPL ChangeLog README NEWS
%{_libdir}/gtk-2.0/*/engines/*.so
%exclude %{_libdir}/gtk-2.0/*/engines/liblighthouseblue.la
%{_datadir}/themes/LighthouseBlue

%changelog
* Wed Jul 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.5
- Rebuild for Fedora
