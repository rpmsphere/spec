%undefine _debugsource_packages
Summary: Document once, include anywhere
Name: doconce
Version: 0.7.3
Release: 5.1
Source0: https://doconce.googlecode.com/files/%{name}-%{version}.tar.gz
License: New BSD
Group: Document
BuildArch: noarch
URL: http://doconce.googlecode.com/
Requires: ImageMagick, python-docutils, python-sphinx, pandoc, ptex2tex, texlive-base, tex-latex
BuildRequires: python2-devel

%description
Doconce is a very simple and minimally tagged markup language that
looks like ordinary ASCII text (much like what you would use in an
email), but the text can be transformed to numerous other formats,
including HTML, Wiki, LaTeX, PDF, reStructuredText (reST), Sphinx,
Epytext, and also plain text (where non-obvious formatting/tags are
removed for clear reading in, e.g., emails). From reStructuredText
you can go to XML, HTML, LaTeX, PDF, OpenOffice, and from the latter
to RTF and MS Word. From Pandoc one can generate Markdown, reST,
LaTeX, HTML, PDF, DocBook XML, OpenOffice, GNU Texinfo, MediaWiki,
RTF, Groff, and other formats.

Doconce is a working strategy for never duplicating information.
Text is written in a single place and then transformed to a number of
different destinations of diverse type (software source code,
manuals, tutorials, books, wikis, memos, emails, etc.). The Doconce
markup language support this working strategy. The slogan is: "Write
once, include anywhere".

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install -O1 --root=$RPM_BUILD_ROOT
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{python2_sitelib}/*
%{_mandir}/man1/*

%changelog
* Sat Jan 26 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.3
- Rebuilt for Fedora
