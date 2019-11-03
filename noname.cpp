///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Aug 22 2019)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

NamaNorma::NamaNorma( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );

	m_panel1 = new wxPanel( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer2;
	bSizer2 = new wxBoxSizer( wxVERTICAL );

	m_staticText1 = new wxStaticText( m_panel1, wxID_ANY, wxT("Tuliskan Nama Norma"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText1->Wrap( -1 );
	bSizer2->Add( m_staticText1, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );

	wxFlexGridSizer* fgSizer1;
	fgSizer1 = new wxFlexGridSizer( 0, 4, 0, 0 );
	fgSizer1->AddGrowableCol( 1 );
	fgSizer1->AddGrowableRow( 0 );
	fgSizer1->SetFlexibleDirection( wxBOTH );
	fgSizer1->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );

	m_staticText2 = new wxStaticText( m_panel1, wxID_ANY, wxT("Nama Norma"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText2->Wrap( -1 );
	fgSizer1->Add( m_staticText2, 0, wxALL|wxALIGN_CENTER_VERTICAL, 5 );

	m_textCtrl_nama_norma = new wxTextCtrl( m_panel1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer1->Add( m_textCtrl_nama_norma, 1, wxALL|wxEXPAND, 5 );

	m_button_ok = new wxButton( m_panel1, wxID_ANY, wxT("Ok"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer1->Add( m_button_ok, 0, wxALL|wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL, 5 );

	m_button_batal = new wxButton( m_panel1, wxID_ANY, wxT("Batal"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer1->Add( m_button_batal, 0, wxALL|wxALIGN_CENTER_VERTICAL, 5 );


	bSizer2->Add( fgSizer1, 0, wxEXPAND, 5 );


	m_panel1->SetSizer( bSizer2 );
	m_panel1->Layout();
	bSizer2->Fit( m_panel1 );
	bSizer1->Add( m_panel1, 1, wxEXPAND | wxALL, 5 );


	this->SetSizer( bSizer1 );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	m_button_ok->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( NamaNorma::m_button_okOnButtonClick ), NULL, this );
	m_button_batal->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( NamaNorma::m_button_batalOnButtonClick ), NULL, this );
}

NamaNorma::~NamaNorma()
{
	// Disconnect Events
	m_button_ok->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( NamaNorma::m_button_okOnButtonClick ), NULL, this );
	m_button_batal->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( NamaNorma::m_button_batalOnButtonClick ), NULL, this );

}
