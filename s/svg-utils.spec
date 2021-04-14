Name:           svg-utils
Version:        0.1
Release:        7.1
Summary:        A Python library for SVG
Group:          Development/Libraries
License:        GPLv3+
URL:            http://programmer-art.org/projects/svg-utils
Source0:        http://programmer-art.org/media/releases/svg-utils/%{name}-%{version}.tar.bz2
BuildRequires:  python2
BuildArch:	noarch

%description
This release of SVG-Utils includes scripts that can dump SVG information,
grayscale and recolor SVG images, and overlay one SVG on top of another.

The library supports creating SVG images on the fly, as well as editing them.
This could be used for server-side scripts using mod_python to send out SVG
data to clients (for generated graphs, for example).

%prep
%setup -q
sed -i '112,117d' install
sed -i -e '/xml.dom.ext/d' -e 's|Print(self.element, outfile)|outfile.write(self.element)|' -e 's|Print(self.element, svg)|svg.write(self.element)|' svg/svgfile.py
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' install *.py svg/*.py

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
./install --prefix=$RPM_BUILD_ROOT/usr --lib-path=$RPM_BUILD_ROOT%{python2_sitelib} --no-symlinks

#sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{python2_sitelib}/svg/*.py %{buildroot}/usr/lib/svg-utils/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/lib/%{name}
%{_datadir}/%{name}
%{python2_sitelib}/svg

%changelog
* Fri Apr 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
