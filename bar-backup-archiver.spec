# TODO
# - unpackaged files
# - create gui subpackage
#
%define		shortname bar
%define		altver b
Summary:	BAR is backup archiver program
Summary(hu.UTF-8):	BAR egy backup archiváló program
Name:		bar-backup-archiver
Version:	0.13
Release:	0.1%{altver}
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://www.kigen.de/projects/bar/bar-%{version}%{altver}.tar.bz2
# Source0-md5:	d2b10480a0c23a7fcd08c2f66c560b17
Patch0:		long_long_max.patch
Patch1:		bar-keygen.patch
URL:		http://www.kigen.de/projects/bar/index.html
BuildRequires:	bzip2-devel
BuildRequires:	ftplib-devel
BuildRequires:	gnutls-devel
BuildRequires:	java-sun-jre
BuildRequires:	java-sun-tools
BuildRequires:	libgcrypt-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	libssh2-devel
BuildRequires:	libtasn1-devel
BuildRequires:	txt2man
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q -n %{shortname}-%{version}%{altver}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure --enable-link-dynamic
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
