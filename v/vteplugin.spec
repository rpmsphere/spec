Name:          vteplugin
Version:       0.1
Release:       7.1
Summary:       A plugin to run a terminal inside a webbrowser tab
Group:         Applications/Web
URL:           https://github.com/arenevier/vteplugin
Source:        https://blog.renevier.net/public/vteplugin-%{version}.tar.bz2
Patch0:         vteplugin-0.1-html.patch
License:       WTFPL
BuildRequires: libpng-devel
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gtk2-devel
BuildRequires: pango-devel
BuildRequires: vte-devel
BuildRequires: python2-devel

%description
vteplugin implements a terminal emulator in a browser plugins.
That means you can use command line in a terminal inside a browser tab.

%prep
%setup -q
%patch 0 -p1
sed -i "s|\(install_path=\"\)|\1$RPM_BUILD_ROOT|;s|\['-O2'\, '-Wall'\]|'%optflags'.split()|" wscript

%build
export CFLAGS="${CFLAGS:-%optflags}" 
export CXXFLAGS="${CXXFLAGS:-%optflags}"
python2 waf configure
python2 waf build

%install
rm -rf $RPM_BUILD_ROOT
python2 waf install

install -D -m0644 vteplugin.html \
   $RPM_BUILD_ROOT%{_datadir}/vteplugin/vteplugin.html

mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib32
mv $RPM_BUILD_ROOT/usr/lib32 $RPM_BUILD_ROOT%{_libdir}

# fixup strange shared library permissions
chmod 755 $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/*.so

%files
%{_libdir}/mozilla/plugins/*.so
%{_datadir}/vteplugin
%doc COPYING.TXT README.TXT

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Thu Apr 15 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.1-1mamba
- package created by autospec
