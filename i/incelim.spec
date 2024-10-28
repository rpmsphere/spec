Summary:   Relax NG Splicer
Name:      incelim
Version:   1.2
Release:   6.1
Source0:   rng-%{name}-%{version}.tar.bz2
Source1:   tests.zip
Patch0:    %{name}.diff
Patch1:    %{name}-readme.diff
License:   Freely distributable
Group:     Productivity/Publishing/XML
BuildRequires: docbook-style-xsl libxslt libxml2
BuildArch: noarch
Requires:  libxslt
URL:       https://ftp.davidashen.net/incelim/

%description
incelim takes a Relax NG grammar in XML syntax, expands all includes
and externalRefs, and optionally replaces references to text, empty,
or notAllowed with the patterns. The result is a 'compiled' schema
convenient for distribution.

The package includes stylesheets for each of the transformation steps,
and two kinds of glue: XSLT stylesheet incelim.xsl, which chains the
transformations using exsl:node-set(), and a shell script, incelim,
which applies each of the stylesheets to the serialized result of the
previous one.

%define INCELIMDIR %{_datadir}/%{name}

%prep
%setup -q -n rng-%{name}-%{version}
%patch 0
%patch 1
[ -e readme.dbx ] && mv readme.dbx readme.xml
mv %{name} %{name}.in
cat %{name}.in | sed s=@INCELIMDIR@=%{INCELIMDIR}= > %{name}
cp %{SOURCE1} .

%build
# Build the HTML page
DB=https://docbook.sourceforge.net/release/xsl/current
# Build HTML from DocBook source
#xmllint --noout --valid readme.xml && \
#xsltproc --nonet --output readme.html  $DB/html/docbook.xsl readme.xml

%install
mkdir -p $RPM_BUILD_ROOT%{INCELIMDIR} \
         $RPM_BUILD_ROOT%{_bindir}
cp -vi *.xsl $RPM_BUILD_ROOT%{INCELIMDIR}/
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}

%files
#doc readme.xml readme.html
%doc readme.txt tests.zip
%dir %{INCELIMDIR}
%{INCELIMDIR}/*.xsl
%{_bindir}/%{name}

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
* Tue May  4 2010 toms@suse.de
- First initial package 1.2
