%undefine _debugsource_packages
Summary: Convert one or more mp3 files into single mp3/m4a/m4b/mp4 file
Name: zak
Version: 0.3
Release: 4.1
Source0: %{name}-%{version}.tar.gz
License: GPLv2
Group: Applications/Multimedia
BuildArch: noarch
URL: http://code.google.com/p/zak/
BuildRequires:  python2
Requires:	gstreamer
Requires:	python2-gstreamer
Requires:	pygtk2
Requires:	madplay
Requires:	ffmpeg
Requires:	vte

%description
Zak allows you to select one or more MP3 files and convert them into a
single MP3 or MP4/M4A/M4B file. The primary use for Zak is audio books.
Most audio books are distributed in several files, usually one per chapter.
Converting these files into a single .m4b allows one to take advantage of
the iPod's bookmarking features.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{python2_sitelib}/zak*
%{_bindir}/zak

%changelog
* Tue Jun 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
* Sat Jan 05 2008 Joshua M. Hoffman <joshua@joshua.net>
- updated to zak 0.3
- 0.3-0
* Thu Jan 03 2008 Joshua M. Hoffman <joshua@joshua.net>
- Initial build
- 0.2-1
