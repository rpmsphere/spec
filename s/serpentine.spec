%undefine _debugsource_packages

Name:           serpentine
Version:        0.7
Release:        1
Summary:        Audio CD Burner
Group:          Applications/Multimedia
License:        GPL
URL:            http://s1x.homelinux.net/projects/serpentine
Source0:        http://download.berlios.de/serpentine/serpentine-%{version}.tar.bz2
Source1:        https://www.iconattitude.com/icons/open_icon_library/apps/png/64/%{name}.png
BuildArch:	noarch
BuildRequires:	pygtk2-devel, GConf2-devel      
BuildRequires:	perl-XML-Parser
BuildRequires:	desktop-file-utils, gettext
Requires:	python2-gstreamer, gnome-python2-nautilus-cd-burner
Requires:	gnome-python2-totem, gnome-python2-gnomevfs, gnome-python2-gconf
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
Serpentine is an application for writing CD-Audio discs. 
It aims for simplicity, usability and compatibility and accepts a big range of
audio (and video) formats thanks to the excelent GStreamer framework. It also
tries to integrate well with other application, accepting full Drag N Drop
from applications like Nautilus, Rhythmbox and even Firefox.

%prep
%setup -q
sed -i -e 's!Terminal=False!Terminal=false!' -e 's|gnome-dev-cdrom-audio|%{name}|' data/serpentine.desktop.in

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --vendor "" --delete-original         \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
	--remove-category X-Ximian-Main                         \
        $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

echo "Name[zh_TW]=蛇紋音樂光碟製作" >> $RPM_BUILD_ROOT%{_datadir}/applications/serpentine.desktop
echo "Comment[zh_TW]=Serpentine 由音樂檔案及清單列表建立音樂光碟" >> $RPM_BUILD_ROOT%{_datadir}/applications/serpentine.desktop
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/serpentine.png

%find_lang %{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%post
update-desktop-database &> /dev/null ||:

%postun
update-desktop-database &> /dev/null ||:

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{python2_sitelib}/serpentine
%{_datadir}/applications/*
%{_datadir}/serpentine
%{_datadir}/pixmaps/serpentine.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7
- Rebuilt for Fedora
* Tue Aug 26 2008 Milo Chen <milo_chen@mail2000.com.tw> - 0.7-6.ossii
- package ossii
- Add zh_TW translation into fedora-serpentine.desktop
* Sat Dec 23 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7-6
- Rebuild with Python 2.5
* Mon Sep 11 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.7-5
- Add missing perl-XML-Parser dependency to fix build
* Tue Sep 07 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.7-4
- Removed %%ghost of .pyo files due to changes in the python packaging guidelines
* Fri Jul 28 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.7-3
- Add missing gnome-python2-gconf dependency to solve #200489
* Sun Apr 02 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.6.91-1
- Initial build
