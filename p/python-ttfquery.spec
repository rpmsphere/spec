%undefine _debugsource_packages
%define oname TTFQuery
%define sname ttfquery

Name: python-%sname
Version: 1.0.5
Release: 3.1
Summary: FontTools-based package for querying system fonts
Group: Development/Python
License: BSD-like
URL: http://ttfquery.sourceforge.net/
Source: %name-%version.tar.gz
BuildArch: noarch
BuildRequires: python2-devel python2-setuptools
#BuildRequires: python2-fonttools

%description
TTFQuery builds on the FontTools package to allow the Python programmer
to accomplish a number of tasks:

  * query the system to find installed fonts
  * retrieve metadata about any TTF font file (even those not yet
    installed)
      o abstract family type
      o proper font name
      o glyph outlines
  * build simple metadata registries for run-time font matching

With these functionalities, it is possible to readily
create OpenGL solid-text rendering libraries which
can accept abstract font-family names as font specifiers
and deliver platform-specific TTF files to match those libraries.

TTFQuery doesn't provide rendering services, but a sample
implementation can be found in the OpenGLContext project, from
which TTFQuery was refactored.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc license.txt doc/index.html
%_bindir/*
%python2_sitelib/%sname/
%python2_sitelib/*egg-info/

%changelog
* Thu Feb 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.5
- Rebuilt for Fedora
* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.bzr20120206
- Snapshot from bzr
- Added module for Python 3
* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1
- Version 1.0.5
* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2.1.1
- Rebuild with Python-2.7
* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.1
- Rebuilt with python 2.6
* Fri Feb 20 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- build as noarch
* Mon Dec 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus
