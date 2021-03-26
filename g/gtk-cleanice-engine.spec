Name:           gtk-cleanice-engine
Version:        2.4.1
Release:        20.1
Summary:        CleanIce GTK Theme Engine
License:        GPL-2.0
URL:            http://sourceforge.net/projects/elysium-project
Group:          System/GUI/GNOME
Source:         gtk-engines-cleanice-%{version}.tar.bz2
BuildRequires:  gtk2-devel

%description
Simple, clean theme engine for GTK2.

%prep
%setup -q -n gtk-engines-cleanice-%{version}

%build
%configure --disable-static
make %{?jobs:-j%jobs}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/gtk-2.0/*/engines/*.so

%changelog
* Sun Mar 24 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.1
- Rebuild for Fedora
* Tue Apr 19 2011 ro@suse.de
- update baselibs.conf
* Sun Jun 14 2009 vuntz@novell.com
- Clean up packaging for Contrib.
* Tue May 13 2008 sbrabec@suse.cz
- Split gtk2-engines-cleanice to a separate package.
- Updated to version 2.4.1:
  * Fix a possible crash.
* Thu Apr 10 2008 ro@suse.de
- added baselibs.conf file to build xxbit packages
  for multilib support
* Wed Sep  6 2006 ro@suse.de
- autoreconf in cleanice to fix build on x86_64
* Sun Feb  6 2005 gekker@suse.de
- Update gtk-engines-cleanice to 2.4.0
* Wed Jun 25 2003 sbrabec@suse.cz
- Added cleanice engine
