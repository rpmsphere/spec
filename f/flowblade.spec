Name:           flowblade
Version:        0.18.0
Release:        5.3
Summary:        Multitrack non-linear video editor
License:        GPLv3
Group:          Video
URL:            https://code.google.com/p/flowblade/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
Requires:       pkgconfig(dbus-python)
Requires:       ffmpeg
Requires:       frei0r-plugins >= 1.4
Requires:       ladspa
Requires:       swh-plugins
Requires:       pkgconfig(cairomm-1.0)
Requires:       mlt
Requires:       librsvg2
Requires:       python2-cairo
Requires:       gnome-python2
Requires:       gnome-python2-gnomevfs
Requires:       pygtk2
Requires:       python-pillow
Requires:       python-mlt
Requires:       python-numpy
Requires:       sox
BuildArch:      noarch

%description
Flowblade is designed to provide a fast, precise and robust editing experience.

In Flowblade clips are usually automatically placed tightly after or between
clips when they are inserted on the timeline. Edits are fine tuned by trimming
in and out points of clips, or by cutting and deleting parts of clips.

Flowblade provides powerful tools to mix and filter video and audio.

%prep
%setup -q
sed -i 's|%{_datadir}/pyshared|%{py_puresitedir}|' flowblade
sed -i "s|respaths.LOCALE_PATH|'%{_datadir}/locale'|g" Flowblade/translations.py

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/locale
mv %{buildroot}%{python_sitelib}/Flowblade/locale/*  %{buildroot}%{_datadir}/locale
find %{buildroot} -type f -name "*.po*" -delete -print

mkdir -p %{buildroot}%{_datadir}/mime/packages
mv %{buildroot}/usr/lib/mime/packages/flowblade \
  %{buildroot}%{_datadir}/mime/packages/

chmod +x %{buildroot}%{python_sitelib}/Flowblade/launch/flowbladebatch \
  %{buildroot}%{python_sitelib}/Flowblade/launch/flowblademedialinker \
  %{buildroot}%{_bindir}/flowblade

chmod -x %{buildroot}%{_datadir}/applications/flowblade.desktop \
  %{buildroot}%{_datadir}/mime/packages/flowblade.xml \
  %{buildroot}%{_datadir}/mime/packages/flowblade


desktop-file-validate %{buildroot}%{_datadir}/applications/flowblade.desktop

%find_lang Flowblade %{name}.lang


%files -f %{name}.lang
%{_bindir}/flowblade
%{_datadir}/applications/flowblade.desktop
%{_mandir}/man1/flowblade.1*
%{_datadir}/pixmaps/flowblade.png
%{python_sitelib}/Flowblade
%{python_sitelib}/flowblade-*.egg-info
%{_datadir}/mime/packages/*

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.18.0
- Rebuilt for Fedora
* Sun Aug 02 2015 abfonly <abfonly@gmail.com> 0.18.0-1
- (233c2b5) Updated flowblade.spec
