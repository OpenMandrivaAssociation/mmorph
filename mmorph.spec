%define name		mmorph
%define version		2.3.4.2
%define version_orig	2.3.4_2
%define release		12

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Morphology tool
Source:		%{name}-%{version_orig}.tar.bz2
Patch0:		%{name}-%{version}.autoconf.patch
Patch1:		%{name}-%{version}.code.patch
Patch2:		%{name}-%{version}-fix-build.patch
Patch3:		mmorph-2.3.4.2-sys_errlist.patch
URL:		http://www.issco.unige.ch/tools
License:	GPL
Group:		Sciences/Computer science
BuildRequires:	db-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A replacement for the old unix crypt(1) command. Mcrypt
uses the following encryption (block) algorithms: BLOWFISH,
DES, TripleDES, 3-WAY, SAFER-SK64, SAFER-SK128, CAST-128, RC2
TEA (extended), TWOFISH, RC6, IDEA and GOST. The unix crypt
algorithm is also included, to allow compatibility with the
crypt(1) command.
CBC, ECB, OFB and CFB modes of encryption are supported.

%prep
%setup -q -n %{name}-%{version_orig}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
autoconf

%build
%configure2_5x
%make CFLAGS="%optflags" DBINCLUDEDIR=/usr/include/db53

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_mandir}
install -d -m 755 %{buildroot}%{_bindir}
%makeinstall MANDIR=%{buildroot}%{_mandir} BINDIR=%{buildroot}%{_bindir} 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc 00CHANGES 00COPYRIGHT 00INSTALL 00INSTALL.configure 00README 00RELEASE_NOTES
%{_bindir}/*
%{_mandir}/man?/*

